import pandas as pd
import numpy as np 
import numpy.linalg as la
import math

def initialize(context):
    #parameters
    context.nobs = 252
    context.recalibrate = 126 #re-estimate every so often (in days)
    context.leverage= 1
    
    #setup the identifiers and data storage
    context.tickers = ['xlf', 'xle', 'xlu', 'xlk', 'xlb', 'xlp', 'xly','xli', 'xlv']
    context.sids = [ sid(19656), sid(19655), 
                       sid(19660), sid(19658), 
                       sid(19654), sid(19659),
                       sid(19662), sid(19657),
                       sid(19661) ]
    context.data = pd.DataFrame({ k : pd.Series() for k in context.tickers } )
    context.mvp = np.array([0]*len(context.tickers))
    context.temp = False
    context.daysToRecalibration = 0
    context.onevec = np.asmatrix(np.ones((len(context.tickers), 1)))
    

def handle_data(context, data):
    if len(context.data.index) < context.nobs:
        #still recording data
        newRow = pd.DataFrame({k:float(data[e].returns()) for k,e in zip(context.tickers, context.sids) },index=[0])
        context.data = context.data.append(newRow, ignore_index = True)
    else:
        newRow = pd.DataFrame({k:float(data[e].returns()) for k,e in zip(context.tickers, context.sids) },index=[0])
        context.data = context.data.append(newRow, ignore_index = True)
        context.data = context.data[1:len(context.data.index)]
            
        if context.daysToRecalibration == 0:
            context.daysToRecalibration = context.recalibrate
            #recalibrate
            log.info('recalibrating...')
            
            #calculate the minimum variance portfolio weights;
            precision = np.asmatrix(la.inv(context.data.cov()))
            pimv = precision*context.onevec / (context.onevec.T*precision*context.onevec)
            pimv = { e:pimv[i,0] for i,e in enumerate(context.tickers) }
            #print pimv    
            #open all positions:
            startingCash = context.portfolio.starting_cash*context.leverage
            for i, e in enumerate(context.sids):
                currentPosition = context.portfolio.positions[e].amount
                newPosition = math.floor(startingCash*pimv[context.tickers[i]]/data[e].price)
                order(e, newPosition - currentPosition)
        else:
            context.daysToRecalibration -= 1

    record(c = context.portfolio.positions_value)
        
        
        