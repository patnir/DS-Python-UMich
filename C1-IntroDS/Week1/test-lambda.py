people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    fullname = person.split(" ")
    title = fullname[0][:-1]
    name = " ".join(fullname[1:])
    return [title, name]


print(list(map(split_title_and_name, people)))

# lambda is an anonymous function


my_function = lambda a, b, c: print(a + b + c)

my_function(1, 2, 3)


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name_lambda(person):
    return person.split()[0] + ' ' + person.split()[-1]


# option 1

func = lambda person: person.split()[0] + ' ' + person.split()[-1]

print(type(func))

for person in people:
    print(split_title_and_name_lambda(person) == func(person))
    # print(split_title_and_name_lambda(person))
    # print(func(person))

# option 2
print(list(map(split_title_and_name_lambda, people)) == list(map(func, people)))

print(list(map(split_title_and_name_lambda, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people)))


def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst


lst = times_tables()
print(lst)

new_lst = [i * j for i in range(10) for j in range(10)]

print(new_lst)
print(lst == new_lst)


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [i + j + k + l for i in lowercase for j in lowercase for k in digits for l in digits]

print(answer[:50])

