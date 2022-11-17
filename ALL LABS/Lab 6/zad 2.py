sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for key in sample_dict:
 print(f'{key:<10}={sample_dict[key]}')

sample_dict = {"name": "Kelly", "surname": "Jones", "age": 25, "salary": 8000, "city": "New york"}
for k in sample_dict:
    print(f'{k:<10}={sample_dict[k]:>8}')
print()
for k, v in sample_dict.items():
    print(f'{k:<10}={v:>8}')


b = ["name", "salary"]
second_sample_dict={}


# for i in b:
#     for j in sample_dict:
#         if i==j:
#             second_sample_dict[i]=sample_dict[i]
#             break
# print(second_sample_dict)


# for i in b:
#     if i in sample_dict.keys():
#         second_sample_dict[i]=sample_dict[i]
# print(second_sample_dict)


second_sample_dict={i:sample_dict[i] for i in b if i in sample_dict.keys()}
print(second_sample_dict)

D = sample_dict.copy()
for k in b:
 if k in D.keys():
  D.pop(k)

if b in D:
 sample_dict.pop()