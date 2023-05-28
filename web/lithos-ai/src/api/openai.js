const API_KEY = "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";
const HEADERS = {
  "Content-Type": "application/json",
  Authorization: `Bearer ${API_KEY}`,
};

export async function completion() {
  const url = "https://api.openai.com/v1/chat/completions";
  const data = {
    model: "gpt-4",
    messages: [{ role: "user", content: "Hello!" }],
  };

  fetch(url, {
    method: "POST",
    headers: HEADERS,
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      // Handle the API response here
      console.log(result.choices[0].message.content);
    })
    .catch((error) => {
      // Handle any errors that occurred during the request
      console.error(error);
    });
}
