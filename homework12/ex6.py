class ListSort:
    def __init__(self,input_list):
        self.input_list = input_list
    def sort_by_height(self):
        people = sorted([x for x in self.input_list if x!= -1])
        result = []
        j = 0
        for i in self.input_list:
            if i == -1:
                result.append(-1)
            else:
                result.append(people[j])
                j += 1
        return result 


input_list = [-1,150,190,170,-1,-1,160,180] 
list_sort = ListSort(input_list)
print(list_sort.sort_by_height())