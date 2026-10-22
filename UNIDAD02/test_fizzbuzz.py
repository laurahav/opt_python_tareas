from fizzbuzz import fizzbuzz

def test_devuelve_numero_como_texto():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_devuelve_fizz_con_multiplos_de_tres():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_devuelve_buzz_con_multiplos_de_cinco():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(50) == "Buzz"

def test_devuelve_fizzbuzz_con_multiplos_de_quince():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(90) == "FizzBuzz"