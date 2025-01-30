В результаті тестування були отримані такі результати:
Test for '100' elements:
Time for insertion_sort: 0.00019212509505450726
Time for merge_sort: 0.00012550002429634333
Time for timsorted: 3.4208991564810276e-05
Time for timsort: 3.233295865356922e-05
Test for '1000' elements:
Time for insertion_sort: 0.018389708013273776
Time for merge_sort: 0.0016332078957930207
Time for timsorted: 0.0003785419976338744
Time for timsort: 0.0003640000941231847
Test for '10000' elements:
Time for insertion_sort: 1.968794749933295
Time for merge_sort: 0.019886124995537102
Time for timsorted: 0.004270167089998722
Time for timsort: 0.004273250000551343

Отже можемо зробити висновок, що метод вставками працює найповільніше. Метод злиттям вже швидший за нього, причому різниця більш відчутна на більшій кількості даних. Та беззаперечно найшвидше працює Timsort. Причому sort дає дещо кращі результати, ніж sorted.