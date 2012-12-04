import java.io.*;
// import java.io.BufferedReader;
// import java.io.BufferedWriter;
// import java.io.FileNotFoundException;
// import java.io.InputStreamReader;
// import java.io.FileInputStream;
// import java.io.FileReader;
// import java.io.OutputStreamWriter;
// import java.io.FileOutputStream;
// import java.io.IOException;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;

/*
Interface for POS-tagging Twitter data.  The function assumes one tweet JSON per line. 
It simply adds a key 'pos' containin the POS-tagged version of the 'text' key.  All 
other values are left in place.

To compile:

javac -cp ".:json-simple-1.1.1.jar:/Volumes/CHRIS/Applications/StanfordNLP/tagger/stanford-postagger.jar" HouseTagger.java

To use:

java -mx3000m -cp ".:json-simple-1.1.1.jar:stanford-postagger.jar" HouseTagger srcFilename outputFilename modelFilename

where modelFilename points to one of the model (.tagger) files in the Tagger distribution.

*/



class HouseTagger {
    
    public static void main(String[] args) throws Exception {
	
	@SuppressWarnings("unchecked")

	final String INPUT_DIR = args[0];
	final String OUTPUT_DIR = args[1];
	final String MODEL_FILE = args[2];
	
	MaxentTagger tagger = new MaxentTagger(MODEL_FILE);
		
	JSONParser parser = new JSONParser();

	File root = new File(INPUT_DIR);
	File[] filenames = root.listFiles();	
	System.out.println("File count: " + filenames.length);
	
	for (int i=0; i < filenames.length; i++) {	
	    
	    if (filenames[i].getName().endsWith(".json")) {	

		System.out.println("Starting " + filenames[i]);
		
		// Read the file into a string:
		BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filenames[i]), "UTF8"));
		StringBuilder builder = new StringBuilder();
		String s = "";
		while ((s = reader.readLine()) != null) {
		    builder.append(s);
		}
		String fileText = builder.toString();

		// Read the file string into JSON:
		Object obj = new Object();
		obj = parser.parse(fileText);
		JSONObject jsonObject = (JSONObject) obj;

		JSONArray transcripts = (JSONArray) jsonObject.get("transcript");
				
		for (int j=0; j < transcripts.size(); j++) {
		    JSONObject turn = (JSONObject) transcripts.get(j);
		    String speech = (String) turn.get("speech");
		    String taggedSpeech = tagger.tagString(speech);
		    turn.put("pos", taggedSpeech);
		}

		jsonObject.put("transcripts", transcripts);
						
		// Create file
		Writer output = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(OUTPUT_DIR + "/" + filenames[i].getName()), "UTF8"));		
		try {
		    output.write(jsonObject.toString() + "\n");
		}
		finally {
		    output.close();
		}

		// // Progress report:
		// System.out.println(i + " " + filenames[i].getName());
	    }
	}
    }
}
