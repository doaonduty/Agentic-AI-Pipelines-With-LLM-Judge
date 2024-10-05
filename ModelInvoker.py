import subprocess
import re

class ModelInvoker:
    """
    A class for invoking models with generated prompts and evaluating their outputs.
    """

    def __init__(self, config, run_judge=False):
        """
        Initializes the ModelInvoker with a configuration dictionary and an optional flag to run the judge model.

        Args:
            config (dict): A dictionary containing model configurations.
            run_judge (bool, optional): A flag to indicate whether to run the judge model. Defaults to False.
        """
        self.config = config
        self.outputs = {}
        self.run_judge = run_judge

    def invoke_model(self, model_name, prompt):
        """
        Invokes a model with the given prompt and stores the output.

        Args:
            model_name (str): The name of the model to invoke.
            prompt (str): The prompt to pass to the model.
        """
        print(f"Running model {model_name}...")
        try:
            output = subprocess.check_output(f"ollama run {model_name} '{prompt}'", shell=True)
            print(f"Model {model_name} completed.")
            self.outputs[model_name] = output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error running model {model_name}: {e}")

    def generate_prompt(self, model_name, num_logs):
        """
        Generates a prompt for the given model based on its configuration.

        Args:
            model_name (str): The name of the model.
            num_logs (int): The number of logs to generate.

        Returns:
            str: The generated prompt.
        """
        print(f"Generating prompt for model {model_name}...")
        model_config = self.config[model_name]
        template_lines = model_config["template_lines"]
        prompt = f"{template_lines}\n\nBased on the templates provided, please generate {num_logs} more new template logs, follow the same format."
        print(f"Prompt generated for model {model_name}.")
        return prompt

    def invoke_model_with_generated_prompt(self, model_name, num_logs):
        """
        Invokes a model with a generated prompt and optionally runs the judge model to evaluate its output.

        Args:
            model_name (str): The name of the model to invoke.
            num_logs (int): The number of logs to generate.
        """
        if model_name!= "judge":
            model_prompt = self.generate_prompt(model_name, num_logs)
            print(f"Running model {model_name} with generated prompt...")
            self.invoke_model(model_name, model_prompt)

            if self.run_judge:
                print(f"Running judge model for {model_name}...")
                judge_prompt = self.generate_judge_prompt(model_name, model_prompt, self.outputs[model_name])
                self.invoke_model("judge", judge_prompt)
                judge_output = self.outputs["judge"]
                self.outputs[model_name] = {
                    f"{model_name}_model_output": self.outputs[model_name],
                    f"{model_name}_judge_prompt": judge_prompt,
                    f"{model_name}_judge_output": judge_output,
                }
                self.add_judge_rating(model_name)

    def add_judge_rating(self, model_name):
        """
        Extracts the judge rating from the judge output and adds it to the model's output dictionary.

        Args:
            model_name (str): The name of the model.
        """
        judge_output = self.outputs[model_name][f"{model_name}_judge_output"]
        match = re.search(r"Total rating: (\d+)", judge_output)
        if match:
            self.outputs[model_name][f"{model_name}_judge_rating"] = int(match.group(1))

    def generate_judge_prompt(self, model_name, model_prompt, model_output):
        """
        Generates a prompt for the judge model based on the model's output and configuration.

        Args:
            model_name (str): The name of the model.
            model_prompt (str): The prompt passed to the model.
            model_output (str): The output of the model.

        Returns:
            str: The generated judge prompt.
        """
        print("Generating judge prompt...")
        model_config = self.config["judge"]
        system_prompt = model_config["system_prompt"]
        model_input = model_prompt
        evaluation_instructions = model_config["evaluation_instructions"]
        template_lines = self.config[model_name]["template_lines"]
        judge_prompt = f"{system_prompt}\n{evaluation_instructions.format(model_input=model_input, model_output=model_output)}\n"
        print(judge_prompt)
        return judge_prompt

    def get_outputs(self):
        """
        Returns the outputs of the models.

        Returns:
            dict: A dictionary containing the outputs of the models.
        """
        print("Getting outputs...")
        return self.outputs