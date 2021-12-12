$total = 0
for (($b = 0); $b -lt 2000; $b++)
{
    $a = $b-1
    if ($a -eq -1) {
        $one = 0
        
    }
    else {
        $one= cat 12.txt | Select -index $a
    }
    $two= cat 12.txt | Select -index $b
    
    if ($one -lt $two)
    {
        $total = $total + 1
        echo "true $($total): $($one), $($two)"
    }
    else
    {
        echo "false $($one), $($two)"
    }
}
echo $total