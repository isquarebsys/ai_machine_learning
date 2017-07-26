import java.io.File;

import net.sourceforge.tess4j.ITesseract;
import net.sourceforge.tess4j.Tesseract;
import net.sourceforge.tess4j.TesseractException;

/**
 * To run the sample, place the tessdata and images under Main Project folder [viz, Tess4J]
 * @author user
 *
 */

public class TesseractExample {
	public static void main(String[] args) {
		File imageFile = new File("D:/ws/search_engine/Tess4J/tessdata/gandhi-pdf-test.png");
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
