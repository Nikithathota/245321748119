from flask import Flask, jsonify
from qualifiedIds import get_primes, get_fibonacci, get_even_numbers,get_random_numbers,average_calculation
app=Flask(__name__)
def get_numbers(number_id):
    count=10
    if number_id.startswith('p'):
        numbers=get_primes(count)
    elif number_id.startwith('f'):
        numbers=get_fibonacci(count)
    elif number_id.startwith('e'):
        numbers=get_even_numbers(count)
    elif number_id.startwith('r'):
        numbers=get_random_numbers(count)
    else:
        return jsonify({"error":"Invalid number ID"}),400
    previous_state=None
    primes=get_primes(count)
    fibonacci=get_fibonacci(count)
    even_numbers=get_even_numbers(count)
    random_numbers=get_random_numbers(count)
    current_state={
        "primes":len(primes),
        "fibonacci": len(fibonacci),
        "even" : len(even_numbers),
        "random": len(random_numbers)
    }
    response={
        "windowprevstate":previous_state,
        "windowcurrstate":current_state,
        "numbers":numbers,
        "avg":average_calculation(numbers),
        "fibonacci":{
            "numbers":fibonacci,
            "avg":average_calculation(fibonacci)
        },
        "even":{
            "numbers":even_numbers,
            "avg":average_calculation(even_numbers)
        },
        "random":{
            "numbers":random_numbers,
            "avg":average_calculation(random_numbers)
        }
    }
    return jsonify(response)
if __name__=='__main__':
    app.run(debug=True)
