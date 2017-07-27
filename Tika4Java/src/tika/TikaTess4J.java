package tika;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import org.apache.tika.exception.TikaException;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.AutoDetectParser;
import org.apache.tika.parser.ParseContext;
import org.apache.tika.parser.Parser;
import org.apache.tika.parser.ocr.TesseractOCRConfig;
import org.apache.tika.parser.pdf.PDFParserConfig;
import org.apache.tika.sax.BodyContentHandler;
import org.xml.sax.SAXException;

/**
 * This file is used to extract PDF Data
 * Caution: Many of the chars in the pdf referred are image like and this DOES NOT extract the text
 * @author user
 *
 */
public class TikaTess4J {

	public static void main(String[] args) {
		Parser parser = new AutoDetectParser();
		BodyContentHandler handler = new BodyContentHandler(Integer.MAX_VALUE);

		TesseractOCRConfig config = new TesseractOCRConfig();
		config.setTesseractPath("D:/ws/git/ai_machine_learning/Tess4J/tessdata");
		
		PDFParserConfig pdfConfig = new PDFParserConfig();
		pdfConfig.setExtractInlineImages(true);

		ParseContext parseContext = new ParseContext();
		parseContext.set(TesseractOCRConfig.class, config);
		parseContext.set(PDFParserConfig.class, pdfConfig);
		// need to add this to make sure recursive parsing happens!
		parseContext.set(Parser.class, parser);

		FileInputStream stream = null;
		Metadata metadata = new Metadata();
		try {
			stream = new FileInputStream(
					"D:/technical/installed/eclipse/neon/pdf/Congress amp Quit India Movement.pdf");
			parser.parse(stream, handler, metadata, parseContext);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SAXException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (TikaException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
//		System.out.println(metadata);
		String content = handler.toString();
		System.out.println("===============");
		System.out.println(content);
//		System.out.println("Done");
	}

}
