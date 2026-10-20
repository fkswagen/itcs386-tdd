# Part B: Reflection

This reflection is based on the code, test results, and commit history of the AI-assisted lab work. Personal observations, especially in questions 2 and 6, should be reviewed by the student before submission.

## 1. Number of tests, production lines, and their ratio

After A8, the final suite contains 9 test functions in `test_kitchen.py`. The production file, `kitchen.py`, contains 40 nonblank lines, or 58 lines including blank lines. The ratio is therefore 9:40, or 0.225 tests per nonblank production line. This counts the final test functions rather than individual assertions and excludes the earlier multiplication-by-two test that was replaced in A3.

## 2. The longest red phase and its cause

The duration of each red phase was not measured, so the longest phase in elapsed time cannot be identified reliably. However, A7 required the most intermediate changes between red and green in the work completed here. The mixed-unit test first failed because `add_rate` did not exist, then returned 201 g instead of 228 g because the amounts were added without conversion. Reaching green required storing rates, passing the converter through `reduce`, and converting each operand before adding.

## 3. Fake It, Triangulate, and Obvious Implementation

Fake It was used in A1 when `times` set the amount to 600, and again in A6 when `plus` returned `grams(500)`. A2 used Triangulate: adding a multiplication-by-two test expecting 400 forced the constant to be replaced with a general multiplication formula. A8 used Obvious Implementation by multiplying both operands of a `Sum` and returning a new `Sum`. Each choice suited its step: Fake It checked the test-to-code connection, Triangulate drove generalization, and Obvious Implementation kept a short, clear change simple.

## 4. Remaining test-list items and next steps

All seven original behaviors, including optional A8, and the additional A7 cases have passing tests. The remaining items concern hashability and behavior when a conversion rate is missing. The next step would be to decide how a missing rate should be reported and write a test for that behavior first. Hashability is speculative because no current requirement uses quantities as dictionary keys or set members, so it should be removed from the immediate work list or deferred rather than adding `__hash__` merely to close an item.

## 5. Would an up-front design have included Quantity.reduce?

An up-front design might have placed all conversion logic in `Converter`, with separate type checks for `Quantity` and `Sum`. A6 and A7 instead showed that both objects could answer `reduce(converter, unit)`: a quantity converts itself, while a sum reduces its operands before adding them. This lets the converter delegate the work and illustrates how the method emerged from concrete test requirements rather than a complete initial design.

## 6. Test-after in Part 0 versus test-first in Part A

Part 0 supplied the production code, so the work focused on checking specified behavior and learning tools such as parametrization, exception assertions, fixtures, and approximate comparisons. Part A started with the API needed by each test and required small implementation changes to satisfy one behavior at a time. The A3 test shaped the design by requiring `times` to return a new object, A4 introduced value equality, and A6-A7 led to `Sum` and converter-aware reduction. A personal comparison of how the two approaches felt should be added by the student based on their own experience performing and reviewing the work.
