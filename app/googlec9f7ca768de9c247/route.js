export async function GET() {
  return new Response("google-site-verification: googlec9f7ca768de9c247.html", {
    headers: { "Content-Type": "text/plain" },
  });
}
