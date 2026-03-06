import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    result = []
    if isinstance(x, list):
        for value in x:
            if isinstance(value, list):
                result_part = []
                for v in value:
                    if v < 0:
                        result_part.append(pow(np.e,v)/(1+pow(np.e,v)))
                    else:
                        result_part.append(1/(1+pow(np.e,-v)))
                result.append(result_part)
            else:
                if value < 0:
                    result.append(pow(np.e,value)/(1+pow(np.e,value)))
                else:
                    result.append(1/(1+pow(np.e,-value)))
        return result
    if x < 0:
        return(pow(np.e,x)/(1+pow(np.e,x)))
    else:
        return(1/(1+pow(np.e,-x)))