first_task - Write a function which accepts time delta specifier as a string argument and returns time
interval in seconds as an integer. Supported time units: s – seconds, m – minute, h – hour, d –
day, with seconds being default unit and one being default value. Supply unit tests for the
solution.

second_task - There are a few text files. You need to write an eternal generator which outputs those files in a
multiplexed file-by- file, line-by- line order. The next line after the last one is the first one. The
next file after the last one is, again, the first one.

third_task - Write generator merge(…) which accepts as arguments an arbitrary number of iterables, each of
which generates sorted numbers, not necessarily one after another. The amount of generated
numbers is not known in advance. merge() must merge the outputs of the iterables, i.e. give
sorted queue of all the numbers from the input iterables. merge() stops when all of the input
iterables have stopped. Please supply unit tests for your solution.
