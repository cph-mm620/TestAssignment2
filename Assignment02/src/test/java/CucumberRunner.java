import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(features = "src/test/resources/features", // Specify your feature file location
        glue = "step_definitions") // Specify the package for your step definitions
public class CucumberRunner {
}