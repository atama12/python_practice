from Utility.common import AnimalInfomation
if __name__ == "__main__":
    animal = AnimalInfomation()
    animal.add_animal("aaa", "哺乳類", ["草原"], "肉食")
    animal.add_animal("ゾウ", "哺乳類", ["森林", "草原"], "草食")
    animal.add_animal("ワシ", "鳥類", ["山地"], "肉食")
    animal.add_animal("カメ", "爬虫類", ["海", "砂漠"], "草食")
    animal.add_animal("クマ", "哺乳類", ["森林"], "食")
    
    print(animal.get_kind_of_animals("哺乳類"))
    
    print(animal.get_habitat_of_animals("森林"))
    
    print(animal.get_diet_ratios())
    