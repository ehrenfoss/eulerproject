<?php

function numberOfDivisors($factorArray) {
	$numberOfDivisors = 1;
	foreach($factorArray as $prime => $power) {
		$numberOfDivisors *= ($power + 1);
	}
	return $numberOfDivisors;
}

function factor($n) {

	$lastFactor = 1;
	$factor = 2;
	$factorArray = array();

	if ($n % 2 == 0) {
		$factorArray["2"]=1;
		$lastFactor = 2;
		$n = $n / 2;
		while ($n % 2 == 0) {
			$factorArray["2"]+=1;
			$n = $n / 2;
		}
	}

	$factor = 3;
	$maxFactor = sqrt($n);

	while ($n > 1 && $factor <= $maxFactor) {
		if (($n % $factor) == 0) {
			$factorArray[$factor]=1;
			//echo "\t".$n."\t".$factor."\n";
			$n = $n / $factor;
			$lastFactor = $factor;
			while (($n % $factor) == 0) {
				$factorArray[$factor]+=1;
				//echo "\t".$n."\t".$factor."\n";
				$n = $n / $factor;
			}
			$maxFactor = sqrt($n);
		}
		$factor = $factor + 2;
	}

	if ($n != 1) {
		$lastFactor = $n;
		$factorArray[$n] = 1;
	}

	return numberOfDivisors($factorArray);
}

$factors = $triangle = $i = $divisors =  0;

while($divisors < 500) {
  $i++;
  $triangle += $i;
  $divisors = factor($triangle);
  echo $triangle."\t".$divisors."\n";
}

