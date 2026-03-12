def increase_salary(salaries):
    new_salary = []
    for salary in salaries:
        updated_salary = salary * 1.1
        new_salary.append(updated_salary)
    return(new_salary)

current_salaries = [1000, 2000, 3000, 4000]
final_salaries = increase_salary(current_salaries)
print(final_salaries)