from typing import List,Dict
class Animal:
    def __init__(self,name:str,kind:str,habitats:List[str],meal:str):
        if not isinstance(name,str):
             raise TypeError(f"Animal's name({name})) is not string type.")
        
        if not isinstance(kind,str):
             raise TypeError(f"Animal's kind({kind}) is not string type.")
        
        if not isinstance(habitats,list) or not all(isinstance(habitat, str) for habitat in habitats):
             raise TypeError(f"Animal's habitats({habitats}) should be a list of strings.")
        
        if not isinstance(meal,str):
             raise TypeError(f"Animal's meal({meal}) is not string type.")
    
        self.__name = name
        self.__kind = kind
        self.__habitats = habitats
        self.__meal = meal
    
    @property
    def name(self):
        return self.__name

    @property
    def kind(self):
        return self.__kind

    @property
    def habitats(self):
        return self.__habitats
    
    @property
    def meal(self):
        return self.__meal
    
class AnimalInfomation:
    def __init__(self):
        self.__animals:List[Animal] = []
        
    def add_animal(self,name:str,kind:str,habitats:List[str],meal:str):
        """
        動物の情報を登録
        @params
         name:動物名
         kind:種類（"哺乳類","爬虫類" etc..)
         habitats:生息地("砂漠","森" etc..)
         meal:食事("肉食","草食","雑食")
        
        @return
         なし
        """
        animal = Animal(name,kind,habitats,meal)
        self.__animals.append(animal)
        
    def get_kind_of_animals(self,targetKind:str) -> List[str]:
        """
        指定した種類の動物名を全て取得
        @params
         targetKind:指定の種類
        
        @return
         matchAnimals:指定した種類の動物名リスト
        """
        if not isinstance(targetKind,str):
            raise TypeError(f"targetKind({targetKind}) is not string type.")
        
        return [animal.name for animal in self.__animals if targetKind == animal.kind]
    
    def get_habitat_of_animals(self,targetHabitat:str) -> List[str]:
        """
        指定した生息地の動物名を全て取得
        @params
         targetHabitat:指定の生息地
        
        @return
         matchAnimals:指定した生息地の動物名リスト
        """
        if not isinstance(targetHabitat,str):
            raise TypeError(f"targetHabitat({targetHabitat}) is not string type.")
        
        
        return [animal.name for animal in self.__animals if targetHabitat in animal.habitats]
    
    def get_diet_ratios(self) -> Dict[str,float]:
        """
        草食、肉食、雑食の割合を取得
        @params
         なし
        
        @return
         dietRatios: 草食、肉食、雑食の割合
        """
        
        animalCounts:int = len(self.__animals)
        
        dietCounts:Dict[str,int] = {"草食":0,"肉食":0,"雑食":0} 

        for animal in self.__animals:
            if animal.meal in dietCounts:
                dietCounts[animal.meal] += 1

        return {
                diet: self.__get_ratios(count,animalCounts)
                for diet,count in dietCounts.items()        
        }

    def __get_ratios(self,dietCount:int,animalCount:int) -> float:
        """
        各食事の割合を取得
        @params
         dietCount:各食事を行う動物の数
         animalCount:動物の総数
        
        @return
         dietCount / animalCount * 100
        """
        if not isinstance(dietCount,int):
            raise TypeError(f"dietCount is not int type.")
        
        if not isinstance(animalCount,int):
            raise TypeError(f"animalCount is not int type.")
        
        if animalCount == 0:
            return 0.0
        
        return dietCount / animalCount * 100