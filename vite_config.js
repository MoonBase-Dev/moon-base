import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/moon-base/', // This is the key line!
  build: {
    outDir: 'dist',
    assetsDir: 'assets'
  }
})