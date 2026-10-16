# AgroVision AI

AI-powered crop disease detection, weather intelligence, and agricultural assistance.

## Run locally

Prerequisite: Node.js 20+.

```bash
npm install
```

Create `.env.local`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Then:

```bash
npm run dev
```

Open `http://localhost:3000`.

## Deploy to Vercel

1. Push this project to GitHub. **Do not commit `.env.local` or any API key.**
2. Import the GitHub repository into Vercel.
3. Keep the Vercel project root set to the folder containing `package.json`.
4. Vercel will use `npm run build` to build the Vite frontend and run the Node/Express server.
5. In Vercel → Project Settings → Environment Variables, add:
   - Name: `GEMINI_API_KEY`
   - Value: your Gemini API key
   - Enable it for the environments you use.
6. Redeploy after adding the variable.

The browser calls `/api/diagnose-crop` and `/api/crop-assistant`; the Gemini key is read only on the server from `process.env.GEMINI_API_KEY`. It is never included in the client bundle.

## Important security note

Never put the Gemini key in frontend code or in variables prefixed with `VITE_`. Never commit `.env.local`.

If a key has already been uploaded to GitHub or shared publicly, revoke/rotate that key and create a new one before deploying.

## GitHub

Recommended files to commit:

- `src/`
- `public/`
- `scripts/`
- `server.ts`
- `package.json`
- `package-lock.json`
- `vite.config.ts`
- `tsconfig.json`
- `vercel.json`
- `.env.example`
- `.gitignore`

Do not commit `node_modules/`, `dist/`, `.env.local`, or any secret.
