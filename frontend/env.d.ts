/// <reference types="vite/client" />
namespace NodeJS {
  interface ProcessEnv {
    readonly VITE_API_BASE_URL: string;
    readonly VITE_APP_MODE: 'development' | 'production' | 'test';
  }
}
