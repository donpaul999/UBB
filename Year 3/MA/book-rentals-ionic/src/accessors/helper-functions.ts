import { AuthenticationStorage } from "../infrastructure";

type httpMethod = "GET" | "POST" | "PUT" | "DELETE"; 

const genericFetch = <T>(method: httpMethod, url: string, body?: any) =>
    new Promise<T>(async (resolve, reject) => {
        const storedValues = await AuthenticationStorage.get();
        try {
            const response = await fetch(url, {
                method,
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${storedValues?.token}` 
                },
                body: JSON.stringify(body)
            });
            if (response.status / 100 === 2) {
                try {
                    resolve(await response.json());
                } catch (e) {
                    resolve(undefined as any);
                }
                return;
            }
            reject(response.status);
        } catch (exception) {
            reject("Could not connect to the server!");
        }
    });

export const httpGet = <T>(url: string, body?: any) => genericFetch<T>("GET", url, body);

export const httpPost = <T>(url: string, body?: any) => genericFetch<T>("POST", url, body);

export const httpPut = <T>(url: string, body?: any) => genericFetch<T>("PUT", url, body);

export const httpDelete = <T>(url: string, body?: any) => genericFetch<T>("DELETE", url, body);

export const getProtocol = async () => {
    const storedValues = await AuthenticationStorage.get();

    return ["access_token", storedValues?.token || ""];
}