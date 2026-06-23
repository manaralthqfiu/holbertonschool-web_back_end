import { uploadPhoto, createUser } from './utils.js';

/**
 * Asynchronously calls uploadPhoto and createUser.
 * 
 * @returns {Promise<Object>} An object with the photo and user responses, or nulls if an error occurs.
 */
export default async function asyncUploadUser() {
  try {
    // Await the resolution of both asynchronous functions
    const photo = await uploadPhoto();
    const user = await createUser();

    // If both succeed, return the combined object
    return {
      photo,
      user,
    };
  } catch (error) {
    // If either function throws an error/rejects, catch it here and return the fallback object
    return {
      photo: null,
      user: null,
    };
  }
}
