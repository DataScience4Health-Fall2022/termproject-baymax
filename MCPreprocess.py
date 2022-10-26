import pandas as pd
data = pd.read_csv('clinvar_conflicting.csv')

def get_variant_list(myList):
  ans = [0, 0, 0]

  if str(myList) == 'nan':
    return ans

  for variant in myList:
    var_str = variant.split('|')[1]
    if var_str == 'missense_variant':
      ans[0] = 1
    elif var_str == 'synonymous_variant':
      ans[1] = 1
    else:
      ans[2] = 1
  return ans

consequences = pd.DataFrame()

consequences['MC'] = data['MC'].str.split(",", n=-1, expand=False)
consequences['variantList'] = consequences['MC'].apply(lambda x: get_variant_list(x))
consequences[['missense_variant', 'synonymous_variant', 'other']] = pd.DataFrame(
            consequences.variantList.tolist(), index=consequences.index)

print(consequences)