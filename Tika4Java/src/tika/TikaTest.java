package tika;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.apache.tika.exception.TikaException;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.AutoDetectParser;
import org.apache.tika.parser.ParseContext;
import org.apache.tika.parser.Parser;
import org.apache.tika.sax.BodyContentHandler;
import org.xml.sax.ContentHandler;
import org.xml.sax.SAXException;


/**
 * This file is used to extract tiff images out of the pdf
 * When run, the tiff is extracted in the same folder as pdf
 * Caution: This is MEMORY consuming and so be cautious about it
 * @author user
 *
 */
public class TikaTest {
	public static void main(String[] args) {
		String target = "D:/technical/installed/eclipse/neon/pdf/Congress amp Quit India Movement.pdf";
		File document = new File(target);
		Parser parser = new AutoDetectParser();
		ContentHandler handler = new BodyContentHandler();
		Metadata metadata = new Metadata();
		try {
			parser.parse(new FileInputStream(document), handler, metadata, new ParseContext());
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (TikaException e) {
			e.printStackTrace();
		}
		System.out.println(metadata);
		System.out.println(handler.toString());
	}
}
