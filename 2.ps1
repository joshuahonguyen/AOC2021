$sum = 0
$total = 0
for (($c = 0); $c -lt 2000; $c++)
{
    $a = $c-2
    $b = $c-1
    $prev = $sum

    if ($a -lt 0)
    {$one = 0}
    else
    {$one= cat 12.txt | Select -index $a}

    if ($b -lt 0)
    {$two = 0}
    else
    {$two= cat 12.txt | Select -index $b}
    $three= cat 12.txt | Select -index $c

    $sum = [int]$one + [int]$two + [int]$three
    if ($a -gt 0 -and $b -gt 0) {
        if ($prev -lt $sum)
        {
            echo "true"
            $total = $total + 1
        }
        else {
            echo "false"
        }
    }
    
}
echo $total