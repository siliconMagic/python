import numpy as np
from pytz import timezone
import scipy

trading_freq = 20

def initialize(context):
    
    context.stocks = [ sid(19662),  # XLY Consumer Discrectionary SPDR Fund
                       sid(19656),  # XLF Financial SPDR Fund
                       sid(19658),  # XLK Technology SPDR Fund
                       sid(19655),  # XLE Energy SPDR Fund
                       sid(19661),  # XLV Health Care SPRD Fund
                       sid(19657),  # XLI Industrial SPDR Fund
                       sid(19659),  # XLP Consumer Staples SPDR Fund
                       sid(19654),  # XLB Materials SPDR Fund
                       sid(19660)]  # XLU Utilities SPRD Fund
    
    context.x0 = 1.0*np.ones_like(context.stocks)/len(context.stocks)

    set_commission(commission.PerShare(cost=0.013, min_trade_cost=1.3))
    
    context.day_count = -1

def handle_data(context, data):
     
    # Trade only once per day
    loc_dt = get_datetime().astimezone(timezone('US/Eastern'))
    if loc_dt.hour == 16 and loc_dt.minute == 0:
        context.day_count += 1
        pass
    else:
        return
    
    # Limit trading frequency
    if context.day_count % trading_freq != 0.0:
        return
    
    prices = history(21,'1d','price').as_matrix(context.stocks)
    ret = prices[1:,:]-prices[0:-1,:] # daily returns
    
    bnds = ((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1))
    cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x)-1.0})
    
    res= scipy.optimize.minimize(variance, context.x0, args=ret,method='SLSQP',constraints=cons,bounds=bnds)
    
    allocation = res.x
    allocation[allocation<0] = 0
    denom = np.sum(allocation)
    if denom != 0:
        allocation = allocation/np.sum(allocation)
    
    for i,stock in enumerate(context.stocks):
        order_target_percent(stock,allocation[i])
        
def variance(x,*args):
    
    p = np.asarray(args)
    Acov = np.cov(p.T)
    
    return np.dot(x,np.dot(Acov,x))