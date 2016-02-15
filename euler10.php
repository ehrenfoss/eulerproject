<?php

$n = 2000000;

function SOE($finish) {

  // Initialise the range of numbers.
  $number = 2;
  $range = range(2, $finish);
  $primes = array_combine($range, $range);
 
  // Loop through the numbers and remove the multiples from the primes array.
  while ($number*$number < $finish) {
    for ($i = $number; $i <= $finish; $i += $number) {
      if ($i == $number) {
        continue;
      }
      unset($primes[$i]);
    }
    $number = next($primes);
  }
  return $primes;
}

function seiveOfEratosthenes($n) {

	$arr = array();

	$primes = array(1,2);

	for ($i = 3;$i <= $n; $i += 2) {
		$arr[$i] = 0;
	}

	var_dump($arr);

	$lastPrime = 3;
	$foundit = true;

	while ($foundit == true) {

		// find the lowest prime not yet processed
		$foundit = false;
		for ($i = $lastPrime; $i <= $n; $i+=2 ) {
			if ($arr[$i] == 0) {
				$arr[$i] = 1;
				$primes[] = $i;
				$lastPrime = $i;
				$foundit = true;
				break;
			}
			echo ".";
		}

		for($i = $lastPrime; $i < $n ; $i += $lastPrime) {
			if (isset($arr[$i])) {
				$arr[$i] = 1;
			}
			echo $i." ".$n."\n";
		}
	}
}

$primes = SOE($n);
$sum = 0;
foreach($primes as $k => $prime) {
	$sum += $prime;
}

echo $sum;
