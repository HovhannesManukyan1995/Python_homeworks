#try:
#    import os
#    import xlsxwriter
#    import argparse
#except ImportError:
#    print('you dont have that kind of modul')
#
#def check_file_existence(fname):
#    os.path.isfile(fname)
#    try:
#        with open(fname) as f:
#                return f.readlines()
#    except OSError as err:
#        print("OS error:", err)
#        exit()
#    except ValueError:
#        print("Could not convert data to an integer.")
#        exit()
#    except Exception as err:
#        print(f"Unexpected {err=}, {type(err)=}")        
#        exit()
#
#def get_human(human_data):
#        tmp = {}
#        human_list = human_data.split()
#        tmp['name'] = human_list[0].strip()
#        tmp['surname'] = human_list[1].strip()
#        tmp['age'] = int(human_list[2].strip())
#        tmp['profession'] = human_list[3].strip()
#        return tmp
#
#def get_humans_list(ml):
#        return [get_human(line) for line in ml if len(line) > 1]
#
#def sort_by_criteria(humans, criteria):
#        if criteria == "surname":
#                humans.sort(key=lambda el: el["surname"])
#        if criteria == "name" :
#                humans.sort(key=lambda el: el["name"])
#        if criteria == "age":
#                humans.sort(key=lambda el: el["age"])
#        if criteria == "profession":
#                humans.sort(key=lambda el: el["profession"])
#        return humans
#
#def write_into_xlsx(fname, content):
#        row = 1
#        column = 0
#        wb = xlsxwriter.Workbook(fname)
#        wsh = wb.add_worksheet()
#        bold = wb.add_format({"bold":1})
#        bold.set_bg_color("#FFFF00")
#        wsh.write("A1" , "Name"  ,bold)
#        wsh.write("B1" , "Surname" , bold)
#        wsh.write("C1" , "Age" , bold)
#        wsh.write("D1" ,"Profession" , bold)
#        wsh.set_column(0, 1, 15)
#        wsh.set_column(0, 3, 15)
#
#        
#        for human in content:
#                wsh.write(row , column , human["name"] )
#                wsh.write(row , column +1 , human["surname"])
#                wsh.write(row , column +2 ,str(human["age"]))
#                wsh.write(row , column +3 ,human["profession"])
#                if human["age"] >= 35:
#                        color1 = wb.add_format({"bg_color":"green"})
#                        wsh.write(row , column , human["name"] , color1 )
#                        wsh.write(row , column +1 , human["surname"],color1)
#                        wsh.write(row , column +2 ,str(human["age"]),color1)
#                        wsh.write(row , column +3 ,human["profession"],color1)
#                row += 1
#        wb.close()
#
#def main():
#        parser = argparse.ArgumentParser()
#        parser.add_argument('-i','--input',help='enter input filename')
#        parser.add_argument('-o','--output',help='enter output filename')
#        parser.add_argument('-so','--sort_option',default='name',
#                help='enter sort option:name,surname,age,profession')
#        args = parser.parse_args()
#        input1=args.input
#        output1=args.output
#        sortop=args.sort_option
#        fname= input1
#        checkf=check_file_existence(fname)
#        humans_list = get_humans_list(checkf)
#        humans_list = sort_by_criteria(humans_list, sortop)
#        write_into_xlsx(output1, humans_list)
#
#main()


#quicksort
import time

start = time.time()
def quick_sort(a):
    if len(a)<2:
        return a
    else:
        lenik=len(a)//2
        tiv=a[lenik]
        poqr=[i for i in a[1:] if i<=tiv]
        mec=[i for i in a[1:] if i>tiv]
        return quick_sort(poqr)+[tiv]+quick_sort(mec)
print(quick_sort([2,345,3453,345346,45,456,54,456,45,5,9,1345,345,3,3,4,6,3,2,34,45,4,3,4,564,6]))
end = time.time() - start
print(end)


start1 = time.time()
def bubbleSort(array):
      for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
          if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
      return array
print(bubbleSort([4,6,4,5,7,43,5354533,66465,454,4,54,6444,34,2,5,9,1,4,6,3,2,34,45,4,3,4,564,6]))  
end1 = time.time() - start1
print(end1)
 



















