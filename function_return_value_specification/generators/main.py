def id_generator(id_gen):
    count = 1
    while id_gen:
        yield f"ID_{count}"
        count+=1

id_gen = id_gen

# Testing the result
for _ in range(5):
    unique_id = next(id_gen)
    print(unique_id)