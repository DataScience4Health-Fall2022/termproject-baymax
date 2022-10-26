import pandas as pd
data = pd.read_csv('clinvar_conflicting.csv')

def get_power_list(num):
  ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  max_power = 9

  if num == 1073741824:
    ans[11] = 1

  elif num == 0:
    ans[0] = 1

  else:
    current_power = max_power
    while current_power >= 0:
      value = 2 ** current_power
      if num >= value:
        num -= value
        ans[current_power+1] = 1
      current_power -= 1

  return ans

origin = pd.DataFrame()
origin['collective_list'] = data['ORIGIN'].apply(lambda x: get_power_list(x))
print(origin)

origin[['unknown', 'germline', 'somatic', 'inherited', 'paternal', 'maternal',
        'de-novo', 'biparental', 'uniparental', 'not-tested',
        'tested-inconclusive', 'other']] = pd.DataFrame(
            origin.collective_list.tolist(), index=origin.index)
print(origin)