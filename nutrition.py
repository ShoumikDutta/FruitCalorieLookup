dic={"apple":"130",
      "avocado":"50",
      "banana":"110",
      "cantaloupe":"50",
      "grapefruit":"60",
      "grapes":"90",
      "honeydew melon":"50",
      "kiwifruit":"90",
      "lemon":"15",
      "lime":"20",
      "orange":"80",
      "nectarine":"60",
      "peach":"60",
      "pear":"100",
      "pineapple":"50",
      "plums":"70",
      "strawberries":"50",
      "sweet cherries":"100",
      "Tangerine":"50",
      "watermelon":"80"  }
s=input("Item: ").lower()
if s in dic:
    print("Calories: "+dic[s])


