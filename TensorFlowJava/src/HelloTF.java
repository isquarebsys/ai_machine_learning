import java.io.UnsupportedEncodingException;

import org.tensorflow.Graph;
import org.tensorflow.Session;
import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;

public class HelloTF {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try (Graph graph = new Graph()) {
			final String value = "Hello from " + TensorFlow.version();

			// Construct the computation graph with a single operation, a
			// constant
			// named "MyConst" with a value "value".
			try (Tensor t = Tensor.create(value.getBytes("UTF-8"))) {
				// The Java API doesn't yet include convenience functions for
				// adding operations.
				graph.opBuilder("Const", "MyConst").setAttr("dtype", t.dataType()).setAttr("value", t).build();
			} catch (Exception e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}

			// Execute the "MyConst" operation in a Session.
			try (
					Session s = new Session(graph); 
					Tensor output = s.runner().fetch("MyConst").run().get(0)) {
				try {
					System.out.println(new String(output.bytesValue(), "UTF-8"));
				} catch (UnsupportedEncodingException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
	}
}
