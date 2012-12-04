#!/bin/bash

# Class path.  Make sure the .jar file points to the tagger jar.
# json-simple-1.1.1.jar is included. Include full path to that too.
cp=.:/Applications/StanfordNLP/tagger/stanford-postagger.jar:json-simple-1.1.1.jar

# This is the model file:
model=/Applications/StanfordNLP/tagger/models/wsj-0-18-caseless-left3words-distsim.tagger

# Source directory:
srcdir=transcripts

# Output directory:
outdir=tagged_transcripts

# First compile:
javac -cp $cp HouseTagger.java

# Now run:
java -mx5000m -cp $cp HouseTagger $srcdir $outdir $model


