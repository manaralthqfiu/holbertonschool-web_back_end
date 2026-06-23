import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
  ]).then((results) => results.map((item) => {
    if (item.status === 'fulfilled') {
      return {
        status: item.status,
        value: item.value
      };
    }
    return {
      status: item.status,
      value: item.reason.toString().replace('Error: ', '')
    };
  }));
}
