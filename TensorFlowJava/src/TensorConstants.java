import org.tensorflow.Graph;
import org.tensorflow.OperationBuilder;
import org.tensorflow.Session;
import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;

public class TensorConstants {

	public static void main(String[] args) {
		try{
		final String value = "Hello from " + TensorFlow.version();
		Tensor tensor = Tensor.create(value.getBytes("UTF-8"));
		Tensor tensor2 = Tensor.create(value.getBytes("UTF-8"));
		Graph graph=new Graph();
		OperationBuilder operationBuilder=graph.opBuilder("Const", "MyConstant");
		operationBuilder.setAttr("dtype", tensor.dataType());
		operationBuilder.setAttr("value", tensor);
		operationBuilder.build();
		Session s = new Session(graph); 
		Tensor output = s.runner().fetch("MyConstant").run().get(0);
		System.out.println("Output as String: "+new String(output.bytesValue()));
		}catch(Exception e){
			System.out.println(e.toString());
		}
	}

}
