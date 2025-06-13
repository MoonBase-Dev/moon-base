import path from 'path';
import { defineConfig, loadEnv } from 'vite';

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      base: '/moon-base/',  // This line is crucial!
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      }
    };
});