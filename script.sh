function clean_file_names {
    find . -name "* *" | awk '{ print length, $0 }' | sort -nr -s | cut -d" " -f2- | while read f
    do base=$(basename "$f")
    newbase="${base// /_}"
    mv "$(dirname "$f")/$(basename "$f")" "$(dirname "$f")/$newbase" 
    done
}

function output_file_name {
    #Set output file name 
    NAME="directory_stats"
    EXT=".txt"
    results_name="$NAME$EXT"
    #Control if the output file already exists and remove the file in case it already exists. 
    if [ -f $results_name ]
    then
    rm $results_name;
    fi
}


args=("$@")

#Remove spaces in folders and files names to avoid error
clean_file_names
#Control if the output file already exists and delete the file in case it does to avoid mixing old with new results.
output_file_name

for i in $(find ${args[0]} -type f);
do
  echo $(ls -la $i | awk '{print $9, $5}') >> $results_name
done;