import numpy as np

def calculate(list):
  if len(list) != 9:
    return ValueError
  result = dict()
  a = np.array(list)
  b = a.reshape((3,3))
  result['mean'] = [b.mean(axis=0).tolist(),b.mean(axis=1).tolist(),b.mean()]
  result['variance'] = [b.var(axis=0).tolist(),b.var(axis=1).tolist(), b.var()]
  result['standard deviation'] = [b.std(axis=0).tolist(), b.std(axis=1).tolist(), b.std()]
  result['max'] = [b.max(axis=0).tolist(),b.max(axis=1).tolist(), b.max()]
  result['min'] = [b.min(axis=0).tolist(),b.min(axis=1).tolist(), b.min()]

  return result