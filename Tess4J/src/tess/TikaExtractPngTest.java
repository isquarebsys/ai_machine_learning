package tess;
import java.io.File;

import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

/**
 * To run the sample, place the tessdata and images under Main Project folder [viz, Tess4J]
 * @author user
 *
 * The workingimage050.png is a file extracted from Tika programs from a pdf
 */

public class TikaExtractPngTest {
	public static void main(String[] args) {
		File imageFile = null;
//		imageFile=new File("D:/ws/git/ai_machine_learning/Tess4J/tessdata/gandhi-pdf-test.png");
//		imageFile=new File("D:/technical/installed/eclipse/neon/pdf/Congress amp Quit India Movement.pdf");
		imageFile=new File("D:/ws/git/ai_machine_learning/Tess4J/tessdata/workingimage050.png");
        ITesseract instance = new Tesseract();  // JNA Interface Mapping
        // ITesseract instance = new Tesseract1(); // JNA Direct Mapping
        try {
            String result = instance.doOCR(imageFile);
            System.out.println(result);
        } catch (TesseractException e) {
            System.err.println(e.getMessage());
        }
	}
}
