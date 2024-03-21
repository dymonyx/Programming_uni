def get_best_results(results):
    new_results = []
    for result in results:  # очистка массива от значений None
        if result != None:
            new_results.append(result)
    mid_result = round(sum(new_results) / len(new_results), 2)
    new_results.sort()  # сортировка массива
    best_results = [new_results[0], new_results[1], new_results[2]]
    return mid_result, *best_results


if __name__ == '__main__':
    results = [None, 22.32, 67.34, 45.21, 53.78, 32.67, None, 56.74, 0.34]
    new_results = get_best_results(results)
    print(f'Средний результат: {new_results[0]}')
    print(f'Лучшие результаты: {new_results[1]}, {new_results[2]}, {new_results[3]}')
