import cucumber.api.java.en.Given;
import cucumber.api.java.en.When;
import cucumber.api.java.en.Then;
import org.junit.Assert;

public class StringUtil {
    private String input;
    private String result = "";
    @Given("a string {string}")
    public void aString(String input) {
        this.input = input;
    }
    @When("I reverse the string")
    public void iReverseTheString() {
        for (int i = input.length()-1; i >= 0; i--) {
            result = result + input.charAt(i);
        }
    }
    @When("I capitalize the string")
    public void iCapitalizeTheString() {
        for (int i = 0; i < input.length(); i++) {
            result = result + String.valueOf(input.charAt(i)).toUpperCase();
        }
    }
    @When("I lowercase the string")
    public void iLowercaseTheString() {
        for (int i = 0; i < input.length(); i++) {
            result = result + String.valueOf(input.charAt(i)).toLowerCase();
        }
    }
    @Then("the result should be {string}")
    public void theResultShouldBe(String expected) {
        Assert.assertEquals(expected, result);
    }
}