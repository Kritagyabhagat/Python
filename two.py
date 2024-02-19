print('Number data types')
a=5
print(type(a))
print(a,type(a))
a=5.5
print(a,type(a))
a=1+2j
print(a,type(a))
print('String data types')
s='Hello@1234'
print(s,type(s))
s="Priyanshu Love Guru"
print(s,type(s))
s='''
Abhishek aur priyanshu 
both partaner 
and roommate
205
'''
print(s,type(s))
s='10'
print(s, type(s))
print('List data type')
l=[10, 'WS', 5.5, 20,30,'abhishek']
print(l, type(l))
l[2]=10
print(l, type(l))
l=['Abhishek']
print(l, type(l))
print('Tuple data type')
t=(10,20,'Hello deepak bhai',25.23,)
print(t,type(t))
print('Dictionary type data')
d={
    'course_name': 'python',
    'course_duration': '2 Month'

}
print(d,type(d))
print('dictionary ke ander ki Value ko get kar sakte ha because Dictionary Key par kam kar ti hai')
print(d['course_name'])
print(d['course_duration'])
B = {'Abhishek': 100, 'Deepak': 80}
print(B, type(B))
print(B['Abhishek'])
print('set data type')
s={10,20,30,10}
print(s,type(s))
s={20,40,50,10,20.5,55.5,100}
print(s,type(s))
s={50,100,150,200,80,90,50}
print(s,type(s))