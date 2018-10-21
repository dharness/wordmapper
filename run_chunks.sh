CHUNK_SIZE=$1
CHUNK_PATH=$2

CHUNK_PARTS_PATH="./chunk-parts"
mkdir chunk-parts
generated_chunks=$(split -l $CHUNK_SIZE $CHUNK_PATH $CHUNK_PARTS_PATH/part_ )

for i in $( ls $CHUNK_PARTS_PATH | grep part ); do
    echo item: $i
    python get_rhymes_async.py --chunk_path="./chunk-parts/$i" &
done
