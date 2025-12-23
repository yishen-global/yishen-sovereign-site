import { NextResponse } from 'next/server'

export async function GET() {
  return new NextResponse(
    `google-site-verification: googlexxxx.html`,
    { headers: { 'Content-Type': 'text/html' } }
  )
}
