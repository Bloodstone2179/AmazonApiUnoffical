api is how you would use the script

amazonApi is the module script

**HOW TO USE**

import amazonApi

amazon = amazonApi.requester('pass in the product code from amzon') //this returns a tuple INDEXS: 0 = price 1 = name 2 = product code 3 = url


**example:**
import AmazonApiUnoffical

code = input("Enter product code:")

re = AmazonApiUnoffical.requester(code)
print("price: " + re[0])

