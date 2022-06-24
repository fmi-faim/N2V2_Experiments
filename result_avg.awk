#!/usr/bin/env awk

NR==1 {
    for (i=1; i<=NF; i++)
        names[i]=$i
    next
}

{ for (i=1; i<=NF; i++) res[i]+=$i }

END {
    print FILENAME

    srt[1]=3; srt[2]=4; srt[3]=1; srt[4]=2;
    for (i=1; i<=NF; i++)
        printf "%16s |", names[srt[i]]
    print ""
    for (i=1; i<=NF; i++)
        printf "%16f |", res[srt[i]]/(NR-1)
    print ""
}
