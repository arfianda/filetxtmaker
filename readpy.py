file1 = open("file1.txt","w")
l = ["Pecel Lele \n","Ayam goreng \n","Ayam Kecap \n"]
file1.writelines(l)
file1.close()

file2 = open("file2.txt", "a")
file2.write("League Of Legends \n")
file2.close()

file3 = open("file3.txt","r")
print("Mahasiswa Universitas Pelita Bangsa")
print(file3.readlines())
print()
file3.close()

file4 = open("file4.txt","w")
file4.write("Call Of Duty \n")
file4.close()

file5 = open("file5.txt","r")
print("Pemuda Bangsa Indonesia")
print(file5.readlines())
print()
file5.close()


