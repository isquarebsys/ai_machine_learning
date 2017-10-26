/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
package ai.api.examples;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import ai.api.AIConfiguration;
import ai.api.AIDataService;
import ai.api.model.AIRequest;
import ai.api.model.AIResponse;

/**
 * Text client reads requests line by line from standard input
 */
public class TextClientApplication {
  private static final String INPUT_PROMPT = "> ";
  public static void main(String[] args) {
    AIConfiguration configuration = new AIConfiguration("9e3b7e0919dc41a2b3228e59b5155d97");
    AIDataService dataService = new AIDataService(configuration);
    String line;
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
      System.out.print(INPUT_PROMPT);
      while (null != (line = reader.readLine())) {
        try {
          AIRequest request = new AIRequest(line);
          AIResponse response = dataService.request(request);
          if (response.getStatus().getCode() == 200) {
            System.out.println(response.getResult().getFulfillment().getSpeech());
          } else {
            System.err.println(response.getStatus().getErrorDetails());
          }
        } catch (Exception ex) {
          ex.printStackTrace();
        }
        System.out.print(INPUT_PROMPT);
      }
    } catch (IOException ex) {
      ex.printStackTrace();
    }
    System.out.println("See ya!");
  }
}
