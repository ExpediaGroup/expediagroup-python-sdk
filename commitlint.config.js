module.exports = {
    extends: ['@commitlint/config-conventional'],
    rules: {
        'header-max-length': [2, 'always', 250],
        'type-empty': [2, 'never'],
        'type-case': [2, 'always', 'lower-case'],
        'type-enum': [2, 'always', ['feat', 'refactor', 'fix', 'docs', 'test', 'chore', 'ci', 'release', 'build']],
        'subject-empty': [2, 'never'],
        'subject-case': [2, 'always', ['sentence-case', 'start-case', 'pascal-case', 'upper-case']],
        'body-leading-blank': [2, 'always'],
        'body-max-line-length': [2, 'always', 100]
    }
};
